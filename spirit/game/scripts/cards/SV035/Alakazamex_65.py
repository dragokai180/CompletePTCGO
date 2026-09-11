from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4b26dd61-8346-5707-ad3a-dc0a33d76c45',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Alakazamex.Name',
    display_name='Alakazam ex',
    searchable_by=['Alakazam ex', 'Stage 2', 'ex', 'Alakazamex'],
    subtypes=['Stage 2', 'ex'],
    collector_number=65,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kadabra.Name',
    family_id=63,
    abilities=[
        Attack(
            title='Mind Jack',
            game_text="This attack does 30 more damage for each of your opponent's Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Dimensional Hand',
            game_text='This attack can be used even if this Pokémon is on the Bench.',
            cost={PokemonTypes.PSYCHIC: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
