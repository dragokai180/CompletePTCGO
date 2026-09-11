from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='371c6cb2-825a-5b74-8c42-edb06571c919',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name',
    display_name='Scyther',
    searchable_by=['Scyther', 'Basic', 'Scyther'],
    subtypes=['Basic'],
    collector_number=65,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=123,
    abilities=[
        Attack(
            title='Cut',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title='Slashing Strike',
            game_text="During your next turn, Scyther can't use Slashing Strike.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
