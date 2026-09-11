from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonToolCardDef(
    guid="9ee6e547-3b9d-546d-9a1c-42ad33b102e2",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VictoryPiece.Name",
    display_name="Victory Piece",
    searchable_by=["Victory Piece","Pokémon Tool","Tool","ACE SPEC","VictoryPiece"],
    subtypes=["Pokémon Tool","Tool","ACE SPEC"],
    collector_number=130,
    set_code="BW8",
    rarity=Rarities.Ace,
    passive=bw_trainer_passive('Victory Piece'),
    granted_abilities=bw_tool_abilities('Victory Piece')
)
