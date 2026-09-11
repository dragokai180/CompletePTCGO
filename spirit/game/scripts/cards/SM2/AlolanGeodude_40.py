from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e3dce8e1-3a60-5d48-a096-2faff6b24550',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGeodude.Name',
    display_name='Alolan Geodude',
    searchable_by=['Alolan Geodude', 'Basic', 'AlolanGeodude'],
    subtypes=['Basic'],
    collector_number=40,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=74,
    abilities=[
        Attack(
            title='Rock Polish',
            game_text='During your next turn, this Pokémon has no Retreat Cost.',
            cost={},
            effect=standard_attack,
        ),
        Attack(
            title='Rollout',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
