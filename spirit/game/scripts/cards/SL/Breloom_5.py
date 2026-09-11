from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e3b08a71-e9dd-5106-b92b-6e8808fe266a',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Breloom.Name',
    display_name='Breloom',
    searchable_by=['Breloom', 'Stage 1', 'Breloom'],
    subtypes=['Stage 1'],
    collector_number=5,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name',
    family_id=285,
    abilities=[
        Attack(
            title='Hibernation Spore',
            game_text="Your opponent's Active Pokémon is now Asleep. Your opponent flips 2 coins instead of 1 between turns. If either of them is tails, that Pokémon is still Asleep.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Magnum Punch',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
