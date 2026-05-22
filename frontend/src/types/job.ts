export interface TrustAnalysis {
  trust_score: number;
  warnings: string[];
}

export interface AnalyzeJobResponse {
  job_title: string;
  company: string;
  trust_analysis: TrustAnalysis;
  ai_analysis: string;
}