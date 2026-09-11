from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f2ba4288-bb53-5cb1-9875-b6a064dd6a64',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Aerodactyl.Name',
    display_name='Aerodactyl',
    searchable_by=['Aerodactyl', 'Stage 1', 'Aerodactyl'],
    subtypes=['Stage 1'],
    collector_number=142,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AntiqueOldAmber.Name',
    family_id=142,
    abilities=[
        Attack(
            title='Glide',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Devolution Ray',
            game_text="If your opponent's Active Pokémon is an evolved Pokémon, devolve it by putting the highest Stage Evolution card on it into your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
