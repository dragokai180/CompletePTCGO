from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.scripts.cards.ME2.Oricorioex_18 import excited_turbo, excited_turbo_condition


card = PokemonCardDef(
    guid="eee10497-b95b-5c85-8936-8e8534b4715c",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorioex.Name",
    display_name="Oricorio ex",
    searchable_by=["Oricorio ex", "Basic", "Oricorioex"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="MEP",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    abilities=[
        Ability(
            title="Excited Turbo",
            game_text="As often as you like during your turn, if you have any [ [Fire] ] Mega Evolution Pokémon ex in play, you may use this Ability. Attach a Basic [ [Fire] ] Energy card from your hand to 1 of your Benched [ [Fire] ] Pokémon.",
            effect=excited_turbo,
            condition=excited_turbo_condition,
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title="Fire Wing",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)
