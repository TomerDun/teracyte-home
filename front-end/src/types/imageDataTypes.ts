export type ImageDataResponse = {
    id: number;
    tc_image_id: string;
    raw_image_path: string;
    created_at: string;
    intensity_average: number;
    classification_label: string;
    processed_image_path: string | null;
    histogram_path: string | null;
    focus_score: number;
}

export type ImageMetadata = {    
    tc_image_id: string;
    created_at: string;
    intensity_average: number;
    classification_label: string;
    focus_score: number;
}

export type ImageHistoryItemType = {
    tc_image_id: string;
    created_at: string;
    classification_label?: string;
}