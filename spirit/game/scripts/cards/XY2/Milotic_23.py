from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='303a029e-e197-520e-b9ea-561f460685e3',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Milotic.Name',
    display_name='Milotic',
    searchable_by=['Milotic', 'Stage 1', 'Milotic'],
    subtypes=['Stage 1'],
    collector_number=23,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name',
    family_id=349,
    abilities=[
        Ability(
            title='Energy Grace',
            game_text='Once during your turn (before your attack) you may Knock Out this Pokémon. If you do, attach 3 basic Energy from your discard pile to 1 of your Pokémon (excluding Pokémon-EX).',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Waterfall',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
