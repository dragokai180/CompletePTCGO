from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8a9449fd-5c18-56c6-9b33-40ec24371d04',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gourgeist.Name',
    display_name='Gourgeist',
    searchable_by=['Gourgeist', 'Stage 1', 'Gourgeist'],
    subtypes=['Stage 1'],
    collector_number=57,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name',
    family_id=710,
    abilities=[
        Attack(
            title='Eerie Voice',
            game_text="Put 2 damage counters each of your opponent's Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Spirit Scream',
            game_text='Put damage counters on both Active Pokémon until the remaining HP of each Pokémon is 10.',
            cost={PokemonTypes.PSYCHIC: 2},
            effect=standard_attack,
        ),
    ],
)
