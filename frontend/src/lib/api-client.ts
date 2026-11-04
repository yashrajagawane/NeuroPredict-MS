export interface ApiConfiguration {
  baseUrl: string;
}

export const apiConfiguration: ApiConfiguration = {
  baseUrl: import.meta.env.VITE_API_BASE_URL ?? "/api/v1",
};

export function apiUrl(path: string, configuration = apiConfiguration): string {
  const baseUrl = configuration.baseUrl.replace(/\/+$/, "");
  const normalizedPath = path.replace(/^\/+/, "");
  return `${baseUrl}/${normalizedPath}`;
}
