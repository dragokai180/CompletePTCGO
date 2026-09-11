from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='58d01e93-4c99-57a6-981c-7b40618d2cbe',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pyukumuku.Name',
    display_name='Pyukumuku',
    searchable_by=['Pyukumuku', 'Basic', 'Pyukumuku'],
    subtypes=['Basic'],
    collector_number=47,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=771,
    abilities=[
        Ability(
            title='Innards Out',
            game_text="If this Pokémon is your Active Pokémon and is Knocked Out by damage from an opponent's attack, put 6 damage counters on the Attacking Pokémon.",
            passive=standard_passive("If this Pokémon is your Active Pokémon and is Knocked Out by damage from an opponent's attack, put 6 damage counters on the Attacking Pokémon."),
        ),
        Attack(
            title='Continuous Tumble',
            game_text='Flip a coin until you get tails. This attack does 30 damage for each heads.',
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
