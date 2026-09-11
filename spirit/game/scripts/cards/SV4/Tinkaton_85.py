from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e89f61fb-a951-5ce1-ae92-2874385f0d39',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tinkaton.Name',
    display_name='Tinkaton',
    searchable_by=['Tinkaton', 'Stage 2', 'Tinkaton'],
    subtypes=['Stage 2'],
    collector_number=85,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name',
    family_id=957,
    abilities=[
        Attack(
            title='Crushing Blow',
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Alloyed Hammer',
            game_text='If this Pokémon has any Metal Energy attached, this attack does 120 more damage.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
