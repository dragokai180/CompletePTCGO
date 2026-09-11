from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='651919cd-d1e2-53cd-9219-6f69a1997b0d',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wormadam.Name',
    display_name='Wormadam',
    searchable_by=['Wormadam', 'Stage 1', 'Wormadam'],
    subtypes=['Stage 1'],
    collector_number=3,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Burmy.Name',
    family_id=412,
    abilities=[
        Attack(
            title='Solar Ray',
            game_text='Heal 20 damage from each of your Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Leaf Cutter',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
