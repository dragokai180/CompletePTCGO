from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c94741f7-ff01-5d7f-ac38-5b4c7edc22cc',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Houndstoneex.Name',
    display_name='Houndstone ex',
    searchable_by=['Houndstone ex', 'Stage 1', 'ex', 'Houndstoneex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=102,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name',
    family_id=971,
    abilities=[
        Attack(
            title='Big Bite',
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Last Respects',
            game_text='This attack does 10 more damage for each Psychic Pokémon in your discard pile.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
