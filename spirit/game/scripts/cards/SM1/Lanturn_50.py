from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='367f89f6-b7f0-590c-9622-de8d584f39eb',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name',
    display_name='Lanturn',
    searchable_by=['Lanturn', 'Stage 1', 'Lanturn'],
    subtypes=['Stage 1'],
    collector_number=50,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name',
    family_id=170,
    abilities=[
        Attack(
            title='Confuse Ray',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Aqua Spark',
            game_text='If this Pokémon has any Water Energy attached to it, this attack does 60 more damage.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
