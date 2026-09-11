from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9a97fa96-b5b3-500b-912d-9e4065def5d7',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Floette.Name',
    display_name='Floette',
    searchable_by=['Floette', 'Stage 1', 'Floette'],
    subtypes=['Stage 1'],
    collector_number=102,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Flabb.Name',
    family_id=669,
    abilities=[
        Attack(
            title='Aromatherapy',
            game_text='Heal 30 damage from each of your Pokémon.',
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Magical Leaf',
            game_text='Flip a coin. If heads, this attack does 20 more damage and heal 20 damage from this Pokémon.',
            cost={PokemonTypes.FAIRY: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
