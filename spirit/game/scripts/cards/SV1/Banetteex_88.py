from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='090314e7-2206-5e08-a48f-36df9496e940',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Banetteex.Name',
    display_name='Banette ex',
    searchable_by=['Banette ex', 'Stage 1', 'ex', 'Banetteex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=88,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name',
    family_id=353,
    abilities=[
        Attack(
            title='Everlasting Darkness',
            game_text="During your opponent's next turn, they can't play any Item cards from their hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Poltergeist',
            game_text='Your opponent reveals their hand. This attack does 60 damage for each Trainer card you find there.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
