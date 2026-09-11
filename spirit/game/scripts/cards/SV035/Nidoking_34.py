from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2ce556fb-0340-5012-83f1-5f99e4608125',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name',
    display_name='Nidoking',
    searchable_by=['Nidoking', 'Stage 2', 'Nidoking'],
    subtypes=['Stage 2'],
    collector_number=34,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name',
    family_id=32,
    abilities=[
        Ability(
            title='Enthusiastic King',
            game_text='If you have Nidoqueen in play, ignore all Energy in the costs of attacks used by this Pokémon.',
            passive=standard_passive('If you have Nidoqueen in play, ignore all Energy in the costs of attacks used by this Pokémon.'),
        ),
        Attack(
            title='Venomous Impact',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=190,
            effect=standard_attack,
        ),
    ],
)
