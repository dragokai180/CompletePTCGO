from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a98d0cdb-3481-56e7-aa79-0ed4d7315e21',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gurdurr.Name',
    display_name='Gurdurr',
    searchable_by=['Gurdurr', 'Stage 1', 'Gurdurr'],
    subtypes=['Stage 1'],
    collector_number=66,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Timburr.Name',
    family_id=532,
    abilities=[
        Attack(
            title='Pummel',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Hammer Arm',
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
