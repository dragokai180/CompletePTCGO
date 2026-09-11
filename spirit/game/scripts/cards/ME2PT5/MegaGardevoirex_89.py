from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="7a21e52e-48f1-56b4-9e77-6575dbc42e90",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaGardevoirex.Name",
    display_name="Mega Gardevoir ex",
    searchable_by=["Mega Gardevoir ex", "Stage 2", "MEGA", "ex", "SV_Mega", "MegaGardevoirex"],
    subtypes=["Stage 2", "MEGA", "ex", "SV_Mega"],
    collector_number=89,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=360,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Attack(
            title="Overflowing Wishes",
            game_text="For each of your Benched Pokémon, search your deck for a Basic Psychic Energy card and attach it to that Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Mega Symphonia",
            game_text="This attack does 50 damage for each Psychic Energy attached to all of your Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=50,
            damage_operator="x",
            effect=standard_attack,
        ),
    ],
)
