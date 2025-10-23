import imageIcon from '../../assets/icons/image-icon.svg';
import intensityIcon from '../../assets/icons/intensity-icon.svg';
import focusIcon from '../../assets/icons/focus-icon.svg';
import tagIcon from '../../assets/icons/tag-icon.svg';
import type { ImageMetadata } from '../../types/imageDataTypes';

type MetadataCardProps = {
  metadata: ImageMetadata | null,
}

export default function MetadataCard({ metadata }: MetadataCardProps) {
  return (
    <div className="bg-white border border-gray-200 rounded-xl h-full w-full flex flex-col gap-12 p-6">
      {/* Header */}
      <div className="shrink-0">
        <h2 className="text-base text-gray-950">Image Metadata</h2>
      </div>

      {/* Metadata Items */}
      <div className="flex flex-col gap-4 shrink-0">
        {/* Image ID */}
        <div className="flex gap-3">
          <img src={imageIcon} alt="" className="size-5 shrink-0" />
          <div className="flex flex-col">
            <p className="text-sm text-[#6a7282]">Image ID</p>
            <p className="text-base text-[#101828]">{metadata ? metadata.tc_image_id : '...'}</p>
          </div>
        </div>

        {/* Intensity Average */}
        <div className="flex gap-3">
          <img src={intensityIcon} alt="" className="size-5 shrink-0" />
          <div className="flex flex-col">
            <p className="text-sm text-[#6a7282]">Intensity Average</p>
            <p className="text-base text-[#101828]">{metadata ? metadata.intensity_average : '...'}</p>
          </div>
        </div>

        {/* Focus Score */}
        <div className="flex gap-3">
          <img src={focusIcon} alt="" className="size-5 shrink-0" />
          <div className="flex flex-col">
            <p className="text-sm text-[#6a7282]">Focus Score</p>
            <p className="text-base text-[#101828]">{metadata ? metadata.focus_score : '...'}</p>
          </div>
        </div>

        {/* Classification */}
        <div className="flex gap-3">
          <img src={tagIcon} alt="" className="size-5 shrink-0" />
          <div className="flex flex-col gap-1">
            <p className="text-sm text-[#6a7282]">Classification</p>
            <span className="inline-flex justify-center px-2 py-0.5 bg-[#d4183d] text-white text-xs rounded-lg w-fit">
              {metadata ? metadata.classification_label : '...'}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}