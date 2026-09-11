from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='25923ee3-c52d-5fee-a30e-17116cbe11c4',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeot.Name',
    display_name='Pidgeot',
    searchable_by=['Pidgeot', 'Stage 2', 'Pidgeot'],
    subtypes=['Stage 2'],
    collector_number=124,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name',
    family_id=16,
    abilities=[
        Attack(
            title='Whirlwind',
            game_text='Your opponent switches their Active Pokémon with 1 of their Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Spin Storm',
            game_text='Your opponent puts their Active Pokémon and all cards attached to it into their hand.',
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
    ],
)
