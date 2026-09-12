from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="187da285-36e6-5ca6-a3bb-7b34e7efaad0",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name",
    display_name="Umbreon",
    searchable_by=["Umbreon","Stage 1","Umbreon","Team Plasma"],
    subtypes=["Stage 1","Team Plasma"],
    collector_number=64,
    set_code="BW9",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    abilities=[
        Ability(
            title="Dark Shade",
            game_text="Each of your Team Plasma Pokémon in play gets +20 HP.",
            passive=bw_legacy_passive("Each of your Team Plasma Pokémon in play gets +20 HP."),
        ),
        Attack(
            title="Darkness Fang",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
