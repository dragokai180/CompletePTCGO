from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dffffad4-042c-55cd-812a-beed156ce630',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wigglytuffex.Name',
    display_name='Wigglytuff ex',
    searchable_by=['Wigglytuff ex', 'Stage 1', 'ex', 'Wigglytuffex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=40,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name',
    family_id=39,
    abilities=[
        Ability(
            title='Expanding Body',
            game_text='If this Pokémon has any Special Energy attached, it gets +100 HP.',
            passive=standard_passive('If this Pokémon has any Special Energy attached, it gets +100 HP.'),
        ),
        Attack(
            title='Friend Tackle',
            game_text='If you played a Supporter card from your hand during this turn, this attack does 90 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
