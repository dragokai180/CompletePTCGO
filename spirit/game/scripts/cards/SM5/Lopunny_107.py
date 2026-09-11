from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='260ec245-10c0-597b-9b2f-ec5db27bab62',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lopunny.Name',
    display_name='Lopunny',
    searchable_by=['Lopunny', 'Stage 1', 'Lopunny'],
    subtypes=['Stage 1'],
    collector_number=107,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name',
    family_id=427,
    abilities=[
        Attack(
            title='Stompy Stomp',
            game_text='Flip 2 coins. This attack does 40 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Happy Turn',
            game_text='You may shuffle this Pokémon and all cards attached to it into your deck.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
