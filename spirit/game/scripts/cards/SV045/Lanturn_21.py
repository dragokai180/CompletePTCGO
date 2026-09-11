from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b3ed1808-c0fb-5bcd-99ce-c25b66f7ea5b',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lanturn.Name',
    display_name='Lanturn',
    searchable_by=['Lanturn', 'Stage 1', 'Lanturn'],
    subtypes=['Stage 1'],
    collector_number=21,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name',
    family_id=170,
    abilities=[
        Attack(
            title='Lightning Ball',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title='Aqua Spark',
            game_text='If this Pokémon has any Water Energy attached, this attack does 120 more damage.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
