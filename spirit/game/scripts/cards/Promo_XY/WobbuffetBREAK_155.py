from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cfa6326d-5738-5944-bcd1-05c9dec05ad1',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.WobbuffetBREAK.Name',
    display_name='Wobbuffet BREAK',
    searchable_by=['Wobbuffet BREAK', 'BREAK', 'WobbuffetBREAK'],
    subtypes=['BREAK'],
    collector_number=155,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name',
    family_id=202,
    abilities=[
        Attack(
            title='Right Back at You',
            game_text="Discard all Energy attached to this Pokémon. During your opponent's next turn, if this Pokémon is damaged by an attack (even if this Pokémon is Knocked Out), put damage counters on the Attacking Pokémon equal to the damage done to this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
