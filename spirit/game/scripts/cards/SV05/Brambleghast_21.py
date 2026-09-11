from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="1b28c3fc-6840-5439-96e9-0b2b87d2c015",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Brambleghast.Name",
    display_name="Brambleghast",
    searchable_by=["Brambleghast", "Stage 1", "Brambleghast"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bramblin.Name",
    family_id=946,
    abilities=[
        Ability(
            title="Resilient Soul",
            game_text="This Pokémon gets +50 HP for each Prize card your opponent has taken.",
            passive=standard_passive("This Pokémon gets +50 HP for each Prize card your opponent has taken."),
        ),
        Attack(
            title="Powerful Needles",
            game_text="Flip a coin for each Energy attached to this Pokémon. This attack does 80 damage for each heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="x",
            effect=standard_attack,
        ),
    ],
)
