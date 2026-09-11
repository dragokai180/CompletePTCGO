from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='880e9d27-f618-51f6-b24b-56eb68a437c6',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name',
    display_name='Gyarados',
    searchable_by=['Gyarados', 'Stage 1', 'Gyarados'],
    subtypes=['Stage 1'],
    collector_number=4,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name',
    family_id=129,
    abilities=[
        Attack(
            title='Hydro Splash',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title='Hyper Beam',
            game_text='Discard an Energy card attached to the Defending Pokémon.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
