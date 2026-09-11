from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f1ee8565-5428-5f43-aadd-e9d823c3f386',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zekrom.Name',
    display_name='Zekrom',
    searchable_by=['Zekrom', 'Basic', 'Zekrom'],
    subtypes=['Basic'],
    collector_number=46,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=644,
    abilities=[
        Attack(
            title='Shred',
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
        Attack(
            title='Bolt Strike',
            game_text='Flip a coin. If tails, this Pokémon does 50 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
