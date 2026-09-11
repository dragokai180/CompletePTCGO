from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bc8383d1-fce0-5448-9221-5d078bbb50ea',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wugtrio.Name',
    display_name='Wugtrio',
    searchable_by=['Wugtrio', 'Stage 1', 'Wugtrio'],
    subtypes=['Stage 1'],
    collector_number=53,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name',
    family_id=960,
    abilities=[
        Ability(
            title='Suddenly Select',
            game_text='When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may search your deck for up to 3 Pokémon Tool cards, reveal them, and put them into your hand. Then, shuffle your deck.',
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Triple Whip',
            game_text='Flip 3 coins. This attack does 70 damage for each heads.',
            cost={PokemonTypes.WATER: 2},
            damage=70,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
