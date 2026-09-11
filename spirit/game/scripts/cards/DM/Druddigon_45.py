from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cb60e472-8f84-5b76-bea8-60b3e2d0bc49',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Druddigon.Name',
    display_name='Druddigon',
    searchable_by=['Druddigon', 'Basic', 'Druddigon'],
    subtypes=['Basic'],
    collector_number=45,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=621,
    abilities=[
        Ability(
            title='Rough Skin',
            game_text="If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), put 3 damage counters on the Attacking Pokémon.",
            passive=standard_passive("If this Pokémon is your Active Pokémon and is damaged by an opponent's attack (even if this Pokémon is Knocked Out), put 3 damage counters on the Attacking Pokémon."),
        ),
        Attack(
            title='Dragon Claw',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
