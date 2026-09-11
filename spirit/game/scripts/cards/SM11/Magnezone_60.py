from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='aef6e168-7436-5b05-b78f-aa8ec465e64b',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name',
    display_name='Magnezone',
    searchable_by=['Magnezone', 'Stage 2', 'Magnezone'],
    subtypes=['Stage 2'],
    collector_number=60,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name',
    family_id=81,
    abilities=[
        Ability(
            title='Double Type',
            game_text='As long as this Pokémon is in play, it is Lightning and Metal type.',
            passive=standard_passive('As long as this Pokémon is in play, it is Lightning and Metal type.'),
        ),
        Attack(
            title='Magnetic Bolt',
            game_text='Put a Trainer card from your discard pile into your hand.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
