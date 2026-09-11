from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_ability, bw_legacy_attack, bw_legacy_passive, bw_stadium_ability, bw_stadium_triggers, bw_tool_abilities, bw_trainer_effect, bw_trainer_passive
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_grass_energy_card

card = PokemonCardDef(
    guid="0c4c6021-054d-5264-8202-8d4cb6872604",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name",
    display_name="Lucario",
    searchable_by=["Lucario","Stage 1","Lucario"],
    subtypes=["Stage 1"],
    collector_number=78,
    set_code="BW8",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    abilities=[
        Ability(
            title="Dual Armor",
            game_text="If this Pokémon has any Metal Energy attached to it, this Pokémon's type is both Fighting and Metal.",
            passive=bw_legacy_passive("If this Pokémon has any Metal Energy attached to it, this Pokémon's type is both Fighting and Metal."),
        ),
        Attack(
            title="Hurricane Kick",
            game_text="Does 30 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
