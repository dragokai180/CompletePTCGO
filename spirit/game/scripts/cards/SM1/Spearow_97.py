from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c0658fc3-69be-51a6-a258-bcc4eb2b4e53',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name',
    display_name='Spearow',
    searchable_by=['Spearow', 'Basic', 'Spearow'],
    subtypes=['Basic'],
    collector_number=97,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=21,
    abilities=[
        Attack(
            title='Peck Bugs',
            game_text="If your opponent's Active Pokémon is a Grass Pokémon, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
