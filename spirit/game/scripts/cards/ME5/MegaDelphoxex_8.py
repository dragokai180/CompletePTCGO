from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="e06e7ddc-ec19-5d51-a610-26ea2593da95",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaDelphoxex.Name",
    display_name="Mega Delphox ex",
    searchable_by=["Mega Delphox ex", "Stage 2", "MEGA", "ex", "SV_Mega", "MegaDelphoxex"],
    subtypes=["Stage 2", "MEGA", "ex", "SV_Mega"],
    collector_number=8,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=350,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name",
    family_id=655,
    abilities=[
        Attack(
            title="Trick Portal",
            game_text="Look at the top 9 cards of your deck, and you may put any number of Pokémon you find there onto your Bench. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Eerie Glow",
            game_text="Your opponent's Active Pokémon is now Burned and Confused.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=standard_attack,
        ),
    ],
)
