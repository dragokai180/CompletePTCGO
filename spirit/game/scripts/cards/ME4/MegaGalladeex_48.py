from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="d20307c9-9f38-5168-b1a5-a16c1f8441a7",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaGalladeex.Name",
    display_name="Mega Gallade ex",
    searchable_by=["Mega Gallade ex", "Stage 2", "MEGA", "ex", "SV_Mega", "MegaGalladeex"],
    subtypes=["Stage 2", "MEGA", "ex", "SV_Mega"],
    collector_number=48,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=350,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=475,
    abilities=[
        Attack(
            title="Gale Slash",
            game_text="If this Pokémon has no damage counters on it, this attack does 150 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            damage_operator="+",
            effect=standard_attack,
        ),
        Attack(
            title="Marvelous Edge",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=240,
        ),
    ],
)
