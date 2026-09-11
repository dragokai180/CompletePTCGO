from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cdff2f0b-5aef-546f-8735-eb09c3b0058f',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slowbro.Name',
    display_name='Slowbro',
    searchable_by=['Slowbro', 'Stage 1', 'Slowbro'],
    subtypes=['Stage 1'],
    collector_number=43,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name',
    family_id=79,
    abilities=[
        Ability(
            title='Strange Behavior',
            game_text='As often as you like during your turn, you may move 1 damage counter from 1 of your other Pokémon to this Pokémon.',
            effect=standard_ability,
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title='Bubble Drain',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
