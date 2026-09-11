from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fae85531-edec-5226-868b-74f21ef99258',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mienshao.Name',
    display_name='Mienshao',
    searchable_by=['Mienshao', 'Stage 1', 'Mienshao'],
    subtypes=['Stage 1'],
    collector_number=97,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Mienfoo.Name',
    family_id=619,
    abilities=[
        Attack(
            title='Three-Step Strike',
            game_text='Flip 3 coins. This attack does 20 damage for each heads.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Whip Expert',
            game_text='If you attached a Pokémon Tool card from your hand to this Pokémon during this turn, this attack does 70 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
