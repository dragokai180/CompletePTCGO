from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='02b7e939-b483-5783-a495-17c9558a45d6',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dustox.Name',
    display_name='Dustox',
    searchable_by=['Dustox', 'Stage 2', 'Dustox'],
    subtypes=['Stage 2'],
    collector_number=28,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cascoon.Name',
    family_id=265,
    abilities=[
        Ability(
            title='Hazardous Evolution',
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may leave your opponent's Active Pokémon Paralyzed and Poisoned. If you do, put 3 damage counters instead of 1 on that Pokémon between turns.",
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Gust',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
