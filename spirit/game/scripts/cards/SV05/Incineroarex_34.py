from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="0eb355a7-6855-50a7-9caf-1c3e7f302718",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Incineroarex.Name",
    display_name="Incineroar ex",
    searchable_by=["Incineroar ex", "Stage 2", "ex", "Incineroarex"],
    subtypes=["Stage 2", "ex"],
    collector_number=34,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name",
    family_id=725,
    abilities=[
        Ability(
            title="Hustle Play",
            game_text="Attacks used by this Pokémon cost Colorless less for each of your opponent's Benched Pokémon.",
            passive=standard_passive("Attacks used by this Pokémon cost Colorless less for each of your opponent's Benched Pokémon."),
        ),
        Attack(
            title="Blaze Blast",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 4},
            damage=240,
            effect=standard_attack,
        ),
    ],
)
