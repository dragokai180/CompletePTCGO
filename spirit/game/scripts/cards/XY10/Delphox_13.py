from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='14fba9ff-18b4-5219-aa2b-e286cec973fb',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Delphox.Name',
    display_name='Delphox',
    searchable_by=['Delphox', 'Stage 2', 'Delphox'],
    subtypes=['Stage 2'],
    collector_number=13,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name',
    family_id=653,
    abilities=[
        Attack(
            title='Flickering Flames',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Psystorm',
            game_text='This attack does 20 damage times the amount of Energy attached to all Pokémon in play.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
