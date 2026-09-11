from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3a9af9c3-103e-5319-bd2b-619fe0c7b341',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoqueen.Name',
    display_name='Nidoqueen',
    searchable_by=['Nidoqueen', 'Stage 2', 'Nidoqueen'],
    subtypes=['Stage 2'],
    collector_number=28,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name',
    family_id=29,
    abilities=[
        Attack(
            title='Return',
            game_text='Draw cards until you have 6 cards in your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Prize Count',
            game_text='If you have more Prize cards left than your opponent, this attack does 50 damage plus 30 more damage.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
