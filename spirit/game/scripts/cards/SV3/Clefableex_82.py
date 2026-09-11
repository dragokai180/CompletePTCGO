from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d5ef30d2-693b-51e7-a508-51a9022faad1',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Clefableex.Name',
    display_name='Clefable ex',
    searchable_by=['Clefable ex', 'Stage 1', 'ex', 'Clefableex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=82,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name',
    family_id=35,
    abilities=[
        Ability(
            title='Lunar Zone',
            game_text='All of your Pokémon that have Psychic Energy attached have no Retreat Cost.',
            passive=standard_passive('All of your Pokémon that have Psychic Energy attached have no Retreat Cost.'),
        ),
        Attack(
            title='Wondrous Moon',
            game_text='You may move any amount of Psychic Energy from your Pokémon to your other Pokémon in any way you like.',
            cost={PokemonTypes.PSYCHIC: 3},
            damage=170,
            effect=standard_attack,
        ),
    ],
)
