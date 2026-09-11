from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1e004985-40ee-54f0-9ba5-dcf904cf40c4',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name',
    display_name='Deoxys',
    searchable_by=['Deoxys', 'Basic', 'Deoxys'],
    subtypes=['Basic'],
    collector_number=2,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=386,
    abilities=[
        Attack(
            title='Cell Storm',
            game_text='Discard 2 Psychic Energy attached to Deoxys and remove 6 damage counters from Deoxys.',
            cost={PokemonTypes.PSYCHIC: 3},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
