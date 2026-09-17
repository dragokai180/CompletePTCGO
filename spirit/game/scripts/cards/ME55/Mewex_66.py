from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6e738228-cc53-5b1f-b24f-8863605081ae',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mewex.Name',
    display_name='Mew ex',
    searchable_by=['Mew ex', 'Basic', 'ex', 'Mewex'],
    subtypes=['Basic', 'ex'],
    collector_number=66,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=151,
    abilities=[
        Ability(
            title='Memory Helix',
            game_text='This Pokémon can use the attacks of any of your Benched Pokémon. (You still need the necessary Energy to use each attack.)',
            passive=standard_passive('This Pokémon can use the attacks of any of your Benched Pokémon. (You still need the necessary Energy to use each attack.)'),
        ),
        Attack(
            title='Teleportation Burst',
            game_text='You may switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
