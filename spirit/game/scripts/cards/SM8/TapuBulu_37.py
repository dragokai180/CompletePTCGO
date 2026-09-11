from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5eca810e-b951-5566-bf78-b94aab755037',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TapuBulu.Name',
    display_name='Tapu Bulu',
    searchable_by=['Tapu Bulu', 'Basic', 'TapuBulu'],
    subtypes=['Basic'],
    collector_number=37,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=787,
    abilities=[
        Attack(
            title='Heavy Punch',
            game_text="This attack does 20 damage for each of your opponent's Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Wild Tackle',
            game_text='Flip a coin. If tails, this Pokémon does 30 damage to itself.',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
