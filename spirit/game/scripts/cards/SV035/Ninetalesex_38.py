from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='21fd84d2-ba9b-51e7-9529-42d0b4539841',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ninetalesex.Name',
    display_name='Ninetales ex',
    searchable_by=['Ninetales ex', 'Stage 1', 'ex', 'Ninetalesex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=38,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name',
    family_id=37,
    abilities=[
        Attack(
            title='Heat Wave',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Mirrored Flames',
            game_text='If you have the same number of cards in your hand as your opponent, this attack does 140 more damage.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
