from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="655ee589-9cdf-5a42-bdc3-441b825eb76d",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGolem.Name",
    display_name="Alolan Golem",
    searchable_by=["Alolan Golem", "Stage 2", "AlolanGolem"],
    subtypes=["Stage 2"],
    collector_number=46,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGraveler.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Electromagnetic Catapult",
            game_text="Flip a coin until you get tails. This attack does 70 damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=70,
            damage_operator="x",
            effect=standard_attack,
        ),
        Attack(
            title="Megaton Fall",
            game_text="This Pokémon also does 40 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
