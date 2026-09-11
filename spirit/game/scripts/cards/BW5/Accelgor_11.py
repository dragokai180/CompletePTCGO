from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="ce916be1-a0d8-5def-9e55-1604833ea30e",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Accelgor.Name",
    display_name="Accelgor",
    searchable_by=["Accelgor","Stage 1","Accelgor"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelmet.Name",
    abilities=[
        Attack(
            title="Hammer In",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Deck and Cover",
            game_text="The Defending Pokémon is now Paralyzed and Poisoned. Shuffle this Pokémon and all cards attached to it into your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=bw_legacy_attack,
        ),
    ],
)
