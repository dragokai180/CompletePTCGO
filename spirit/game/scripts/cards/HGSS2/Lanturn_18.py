from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6963a3ba-c8bf-5c17-a7d3-19c6921667a4',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name',
    display_name='Lanturn',
    searchable_by=['Lanturn', 'Stage 1', 'Lanturn'],
    subtypes=['Stage 1'],
    collector_number=18,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name',
    family_id=170,
    abilities=[
        Attack(
            title='Confuse Ray',
            game_text='Flip a coin. If heads, the Defending Pokémon is now Confused.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Reflect Energy',
            game_text='Move an Energy card attached to Lanturn to 1 of your Benched Pokémon.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
